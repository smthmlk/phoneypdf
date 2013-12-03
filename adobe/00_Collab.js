//////////////////////////////////////////////////////////////////////////
/*
 phoneyPDF
 Collab Object
 Kiran Bandla <kbandla@intovoid.com>
 */

var Collab = {};

Collab.AlertWithHelpWidth = 508; // number
Collab.addedAnnotCount = 0; // number
Collab.buttonRowMarginHeight = 11; // number
Collab.buttonRowMarginWidth = 11; // number
Collab.defaultStore = 'NONE'; // string
Collab.docID = '3thGgdtqRf1MJuCEBinNqC'; // string
Collab.hasSynchonizer = true; // boolean
Collab.initiatorEmail = undefined; // undefined
Collab.isDocCtrInitAvailable = true; // boolean
Collab.isOutlook = false; // boolean
Collab.marginHeight = 20; // number
Collab.marginWidth = 20; // number
Collab.modifiedAnnotCount = 0; // number
Collab.navIconHeight = 12; // number
Collab.navIconWidth = 12; // number
Collab.privateAnnotsAllowed = false; // boolean
Collab.showAnnotToolsWhenNoCollab = false; // boolean
Collab.showBasicAuditTrail = false; // boolean
Collab.tipIconHeight = 32; // number
Collab.tipIconWidth = 32; // number
Collab.wizardHeight = 428; // number
Collab.wizardMarginWidth = 25; // number
Collab.wizardWidth = 575; // number

function_list = ['init','sync','animateSyncButton','takeOwnershipOfComments','addAnnotStore','createAnnotStore','newWrStreamToCosObj','stream2CosObj','cosObj2Stream','URL2PathFragment','hashString','getStoreSettings','setStoreSettings','getStoreFSBased','setStoreFSBased','getStoreNoSettings','setStoreNoSettings','documentToStream','streamToDocument','addStateModel','removeStateModel','getStateModels','registerReview','unregisterReview','setReviewRespondedDate','registerProxy','getProxy','canProxy','createUniqueDocID','alertWithHelp','registerApproval','unregisterApproval','makeAllCommentsReadOnly','removeApprovalDocScript','beginInitiatorMailOperation','endInitiatorMailOperation','isOnlineReview','isOfflineReview','isEmailReview','isApprovalWorkflow','isSharedReview','getReviewFolder','setReviewFolder','setReviewFolderForMultipleReviews','addReviewFolder','removeReviewFolder','getReviewFolders','unregisterOffline','browseForNetworkFolder','browseForFolder','convertMappedDrivePathToSMBURL','mountSMBURL','uriEncode','uriNormalize','uriConvertReviewSource','uriToDIPath','uriCreateFolder','uriDeleteFolder','uriPutData','uriEnumerateFiles','uriDeleteFile','isPathWritable','stringToUTF8','launchHelpViewer','swConnect','swSendVerifyEmail','swAcceptTOU','swRemoveWorkflow','getCCaddr','hasInitiatorEmailRequest','finalApprovalEmailEnabled','enableFinalApprovalEmail','isUbiquitized','getIdentity','goBackOnline','bringToFront','getFdfUrl','updateMountInfo','addReviewServer','setDefaultReviewServer','getAlwaysUseServer','setAlwaysUseServer','unsetAlwaysUseServer','setERTCWelcomeInvisible','unsetERTCWelcomeInvisible','getCustomEmailMessage','setCustomEmailMessage','getReviewInfo','returnToInitiator','convertDIPathToPlatformPath','convertPlatformPathToDIPath','getAggregateReviewInfo','getNumberOfReviewsOnServer','removeMultipleSelectedReviewsInTracker','expandTrackerSelection','collapseTrackerSelection','hasReviewCommentRepositoryIntact','hasReviewDeadline','getReviewState','getReviewError','isDocCenterURL','getServiceURL','saveTrackerHTML','dumpTrackerHTML','getSelectedNodeHierarchy','allReviewServers','docCenterLogin','shareFileBezel','dcSignup','shareFile','getDateAndTime','getDefaultDateAndTime','AVUMLogEventWrapper','AVUMStartPayloadWrapper','AVUMEndPayloadWrapper','AVUMAddStringToPayloadWrapper','AFPrepareFormForDistribution','AFCheckSubmitButtonStatus','GetActiveDocIW','getDocCenterReviewServer','getEmailDistributionReviewServer','isDocDirty','isFirstLaunch','unsetFirstLaunch','takeOwnershipAndPublishComments','getFullyQualifiedHostname','getProgressInfo','getUserIDFromStore','addDocToDocsOpenedByWizard','removeDocsOpenedByWizard','isDocReadOnly','invite','collectEmailInfo','getIcon'];

///////// Reader-like implementations ;)
/*
Collab.invite = function ANDefaultInvite(doc, bUpdate, decodedURL) {
        if (!doc.external) {
                    return ANSendForReview(doc, bUpdate);
                        }
            return CBBBRInvite(doc, decodedURL);
};
*/
//////// Specific functions
/*
Collab.collectEmailInfo = function(){
        for( i in arguments){
            console.log(typeof(arguments[i]));
            console.log(arguments[i]);
            if (typeof(arguments[i]) == 'object'){
                for(x in arguments[i]){
                    console.info(x);
                }
            }
            console.warn('collectEmailInfo : ##################');
        }
};
Collab.getIcon = function(){
    log_event('CVE-2009-0927');
};
*/
//////// Generic funciton handlers
/*
for( temp in function_list ){
    if ( !Collab.hasOwnProperty( function_list[temp] ) ){
        Collab[function_list[temp]] = new Function(" var args = [];             \
                for(i in arguments){                                            \
                    if( typeof(arguments[i]) == 'object') {                     \
                        for( x in arguments[i]){                                \
                            args.push(arguments[i][x]);                         \
                        }                                                       \
                    }else{                                                      \
                        console.log('TYPE = '+typeof(arguments[i]));            \
                        args.push(arguments[i]);}                               \
                }                                                               \
                args.pop();  log_event('Collab.'+'"+function_list[temp]+"', args);");
    }//if
}//for
*/
handleObjectHooks(Collab, function_list, 'Collab');
